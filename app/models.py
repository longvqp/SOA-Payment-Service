from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from . import db,login_manager
from random import randint

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    masv = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    sdt = db.Column(db.String(10), unique=True) #?
    password_hash = db.Column(db.String(128))
    sodu = db.Column(db.Float, default=0)
    hocphi = db.relationship('HocPhi', backref='users', lazy=True)
    lichsu = db.relationship('LichSu', backref='users', lazy=True)  
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

   
    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def __repr__(self):
        return '<User %r>' % self.username




class HocPhi(db.Model):
    __tablename__ = 'hocphis'
    id = db.Column(db.Integer, primary_key=True)
    masv = db.Column(db.String(64), db.ForeignKey('users.masv'), nullable=False)
    term = db.Column(db.String(64),  unique=True, nullable=False)
    sotien = db.Column(db.Float, nullable=False, default=0)
    otp = db.Column(db.String(6),unique=True)
    status = db.Column(db.String(10), nullable=False , default='Wait')
    lichsu = db.relationship('LichSu', backref='hocphis', lazy=True)
    
    def generate_confirmation_otp(self, expiration=300):
        s = Serializer(self.otp, expiration)
        return s.dumps({'otp' : otp}).decode('utf-8')

    def confirm(self, otp):
        s = Serializer(t)
        try:
            data = s.loads(otp.encode('utf-8'))
        except:
            return False
        if data.get('user') != self.id | data.get('otp') != s:
            return False
        self.status = 'Done'
        return True

    def generate_reset_otp(self, expiration=300):
        t =  "%06d" % randint(0,999999)
        self.otp = t
        s = Serializer(t, expiration)
        return s.dumps({'reset': self.id , 'otp': t}).decode('utf-8')


class LichSu(db.Model):
    __tablename__ = 'histories'
    id = db.Column(db.Integer, primary_key=True)
    hocphi_id = db.Column(db.Integer , db.ForeignKey('hocphis.id'), nullable=False)
    masv_nop  =  db.Column(db.String(64), db.ForeignKey('users.masv'), nullable=False)
    # masv_no = db.Column(db.String(64), db.ForeignKey('hocphis.masv'), nullable=False, index=True)
    # Mã số sinh viên nợ được lưu ở bảng học phí rồi nên không lưu ở đây nữa/ sinh lỗi AmbiguousForeignKeys
    timestamp = db.Column(db.DateTime)


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False
login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
