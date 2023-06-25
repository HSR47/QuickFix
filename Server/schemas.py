

from pydantic import BaseModel , constr
from datetime import datetime

# ----------------------------LOGIN SCHEMA-------------------------
class login(BaseModel):
    email : constr(regex=r'^.+@iiitm\.ac\.in$')
    password : str
    type : constr(regex=r'^(student|admin)$')

class changePassword(BaseModel):
    oldPassword : str
    newPassword : str

class sendOtp(BaseModel):
    email : constr(regex=r'^.+@iiitm\.ac\.in$')
    type : constr(regex=r'^(student|admin)$')

class verifyOtp(BaseModel):
    email : constr(regex=r'^.+@iiitm\.ac\.in$')
    type : constr(regex=r'^(student|admin)$')
    otp : constr(regex=r'^[0-9][0-9][0-9][0-9][0-9]$')

class changePasswordForgot(BaseModel):
    newPassword : str
    token : str
# ------------------------------------------------------------------


# ----------------------------STUDENT SCHEMAS-------------------------
class signupStudent(BaseModel):
    name : str
    email : constr(regex=r'^.+@iiitm\.ac\.in$')
    hostel : constr(regex=r'^(bh1|bh2|bh3|gh)$')
    room : str
    password : str

class updateStudent(BaseModel):
    name : str | None
    hostel : constr(regex=r'^(bh1|bh2|bh3|gh)$') | None
    room : str | None

class returnStudent(BaseModel):
    id : int
    name : str
    email : str
    hostel : str
    room : str
    verified : str
    created : datetime

    class Config():
        orm_mode = True
# ------------------------------------------------------------------


# ----------------------------ADMIN SCHEMAS-------------------------
class signupAdmin(BaseModel):
    name : str
    email : constr(regex=r'^.+@iiitm\.ac\.in$')
    hostel : constr(regex=r'^(bh1|bh2|bh3|gh)$')
    password : str

class updateAdmin(BaseModel):
    name : str | None
    hostel : constr(regex=r'^(bh1|bh2|bh3|gh)$') | None

class returnAdmin(BaseModel):
    id : int
    name : str
    email : str
    hostel : str
    created : datetime

    class Config():
        orm_mode = True
# ------------------------------------------------------------------


# ----------------------------PERSONAL COMPLAINT SCHEMA-------------------------
personalElectricalObjects = [
    "tubelight",
    "seconday light",
    "switch board",
    "fan",
    "fan regulator"
]

personalCarpentryObjects = [
    "table",
    "chair",
    "bed",
    "door",
    "cupboard",
    "window",
    "curtain hanger"
]

class createPersonalComplaint(BaseModel):
    title : str
    description : str
    category : constr(regex=r'^(electrical|carpentry)$')
    object : constr(regex=r'^(' + "|".join(personalCarpentryObjects + personalElectricalObjects) + r')$')
    password : str

# ------------------------------------------------------------------



# ----------------------------COMMON COMPLAINT SCHEMA-------------------------
commonElectricalObjects = [
    "water cooler"
]

commonCarpentryObjects = [
    "bathroom door"
]

commonPlumbingObjects = [
    "toilet seat",
    "flush",
    "tap",
    "urinal",
    "geaser",
    "shower",
    "basin",
    "other"
]

possibleObjectId = [
    "GroundFloor",
    "Floor1",
    "Floor2",
    "Floor3",
    "Toilet1",
    "Toilet2",
    "Toilet3",
    "Toilet4",
    "Toilet5",
    "Toilet6",
    "Toilet7",
    "Toilet8",
    "Toilet9",
    "Toilet10",
    "Toilet11",
    "Toilet12",
    "Toilet13",
    "Toilet14",
    "Toilet15",
    "Toilet16",
]


class createCommonComplaint(BaseModel):
    title : str
    description : str
    category : constr(regex=r'^(electrical|carpentry|plumbing)$')
    location : constr(regex=r'^(bh1|bh2|bh3|gh)$')
    object : constr(regex=r'^(' + "|".join(commonCarpentryObjects + commonElectricalObjects + commonPlumbingObjects) + r')$')
    objectId : constr(regex=r'^(' + "|".join(possibleObjectId) + r')$')
    password : str

# ------------------------------------------------------------------



# ----------------------------RETURN COMPLAINTS SCHEMA-------------------------
class returnStudentInComplaint(BaseModel):
    id : int
    name : str
    email : str
    hostel : str
    room : str

    class Config():
        orm_mode = True

class requestRejectReason(BaseModel):
    reason : str

class returnRejectReason(BaseModel):
    reason : str

    class Config():
        orm_mode = True

class returnWhoUpvoted(BaseModel):
    studentId : int

    class Config():
        orm_mode = True

class returnImageInComplaint(BaseModel):
    name : str
    url : str

    class Config():
        orm_mode = True

class returnComplaint(BaseModel):
    id : int
    title : str
    description : str
    state : str
    type : str
    category : str
    location : str
    object : str
    objectId : str
    created : datetime
    student : returnStudentInComplaint
    rejectReason : returnRejectReason | None
    whoUpvoted : list[returnWhoUpvoted]
    image : returnImageInComplaint | None

    class Config():
        orm_mode = True
# ------------------------------------------------------------------



# ----------------------------EMAIL SCHEMA-------------------------
class email(BaseModel):
    email: constr(regex=r'^.+@iiitm\.ac\.in$')
# ------------------------------------------------------------------
