python
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from src.utils import get_password_hash, verify_password

class Usuario(BaseModel):
    id: int
    nome: str
    email: Optional[EmailStr]
    senha: str
    ativo: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str]

class RegisterUsuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    ativo: bool

    class Config:
        orm_mode = True

class LoginUsuario(BaseModel):
    email: EmailStr
    senha: str

    class Config:
        orm_mode = True

class UsuarioDB(Usuario):
    senha_hash: str

class UsuarioSchema(usuarioBase = Usuario):
    senha: str

class UsuarioBaseSchema(usuarioBase ):
    senha_hash: str

    @property
    def senha( self ):
        raise AttributeError('Senha não acessível')
    
    @senha.setter
    def senha(self, senha ):
        self.senha_hash = senha
    
    def verify_password(self, senha ):
        return verify_password( senha, self.senha )

    class Config:
        orm_mode = True

class RoleBase:
    id: int
    nome: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    nome: str
    usuarios: List['Usuario']

class UsuarioRole(usuarioBase):
    role_id: int
    role: Role

class UsuarioRoleCreate(BaseModel):
    usuario_id: int
    role_id: int
