
// Add event listener to form submit
document.querySelector("form").addEventListener("submit", function(event) {
   // Prevent default form submission
   event.preventDefault();
   
   // Get input values
   var name = document.querySelector("#name").value;
   var email = document.querySelector("#email").value;
   var message = document.querySelector("#message").value;
   
   // Validate input values
   if (name === "") {
      alert("Please enter your name");
      return;
   }
   
   if (email === "") {
      alert("Please enter your email");
      return;
   }
   
   if (message === "") {
      alert("Please enter your message");
      return;
   }
   
   // Send form data to server (replace with actual server code)
   console.log("Form submitted:");
   console.log("Name: " + name);
   console.log("Email: " + email);
   console.log("Message: " + message);
});

// Add event listener to navigation links
document.querySelectorAll("nav ul li a").forEach(function(link) {
   link.addEventListener("click", function(event) {
      event.preventDefault();
      
      // Get section ID
      var sectionId = link.getAttribute("href").split("#")[1];
      
      // Scroll to section
      document.querySelector("#" + sectionId).scrollIntoView();
   });
});
