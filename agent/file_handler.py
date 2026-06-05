import os
import re
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

class FileHandler:
    """
    Handles parsing raw LLM output to detect and extract code blocks, 
    and saves them automatically as files.
    """
    def __init__(self):
        self.output_dir = Config.OUTPUT_DIR
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def extract_and_save_files(self, text: str, task_id: int) -> list:
        """
        Detects markdown code blocks, attempts to infer filenames or generates one,
        and saves the files to disk. Returns a list of created file paths.
        """
        # Matches ```<language> (optional filename hint)\n <code> ```
        # We will keep it simple and just look for ```language ... ```
        pattern = re.compile(r"```([\w+]+)?\n(.*?)```", re.DOTALL)
        matches = pattern.findall(text)
        
        saved_files = []
        
        # We also try to look for obvious file name markers in the text like File: index.html
        filename_pattern = re.compile(r"(?:File|Filename|file):\s*([a-zA-Z0-9_\-\.]+)")
        possible_filenames = filename_pattern.findall(text)

        for i, match in enumerate(matches):
            language = match[0].strip().lower() if match[0] else 'txt'
            code = match[1].strip()
            
            # Map common languages to extensions
            ext_map = {'python': 'py', 'javascript': 'js', 'html': 'html', 'css': 'css', 'json': 'json', 'bash': 'sh', 'sh': 'sh'}
            ext = ext_map.get(language, language or "txt")
            
            # Determine filename
            if i < len(possible_filenames):
                filename = possible_filenames[i]
            else:
                filename = f"task_{task_id}_output_{i+1}.{ext}"
                
            filepath = os.path.join(self.output_dir, filename)
            
            # Write to disk
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)
                
            saved_files.append(filepath)
            
        return saved_files
