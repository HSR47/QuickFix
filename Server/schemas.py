

from pydantic import BaseModel , constr , Field , validator
from datetime import datetime

# ----------------------------LOGIN SCHEMA-------------------------
class login(BaseModel):
    email : constr(regex=r'^(bcs|imt|img)_20[12][0-9][01][0-9][0-9]@iiitm\.ac\.in$')
    password : str
    type : constr(regex=r'^(student|admin)$')

class changePassword(BaseModel):
    oldPassword : str
    newPassword : str

class sendOtp(BaseModel):
    email : constr(regex=r'^(bcs|imt|img)_20[12][0-9][0-9][0-9][0-9]@iiitm\.ac\.in$')
    type : constr(regex=r'^(student|admin)$')

class verifyOtp(BaseModel):
    email : constr(regex=r'^(bcs|imt|img)_20[12][0-9][0-9][0-9][0-9]@iiitm\.ac\.in$')
    type : constr(regex=r'^(student|admin)$')
    otp : constr(regex=r'^[0-9][0-9][0-9][0-9][0-9]$')

class changePasswordForgot(BaseModel):
    newPassword : str
    token : str
# ------------------------------------------------------------------


# ----------------------------STUDENT SCHEMAS-------------------------
class signupStudent(BaseModel):
    name : str
    email : constr(regex=r'^(bcs|imt|img)_20[12][0-9][0-9][0-9][0-9]@iiitm\.ac\.in$')
    hostel : constr(regex=r'^(bh1|bh2|bh3|gh)$')
    room : int = Field(ge=1 , le=400)
    password : str = Field(min_length=6)

    @validator('name')
    def trim_whitespace(cls, value:str):
        return value.strip()

class updateStudent(BaseModel):
    name : str | None
    hostel : constr(regex=r'^(bh1|bh2|bh3|gh)$') | None
    room : int | None = Field(ge=1 , le=400)

    @validator('name')
    def trim_whitespace(cls, value:str):
        if value == None:
            return None
        return value.strip()

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

    @validator('name')
    def trim_whitespace(cls, value:str):
        return value.strip()

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
    "secondary light",
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

    @validator('title' , 'description')
    def trim_whitespace(cls, value:str):
        return value.strip()
# ------------------------------------------------------------------



# ----------------------------COMMON COMPLAINT SCHEMA-------------------------
commonElectricalObjects = [
    "water cooler",
    "geaser",
    "bathroom tubelight",
    "bathroom switchboard",
    "bathroom exhaut fan"
]

commonCarpentryObjects = [
    "bathroom door",
]

commonPlumbingObjects = [
    "toilet seat",
    "flush",
    "tap",
    "urinal",
    "shower",
    "basin",
]

possibleObjectId = [
    "GroundFloor",
    "Floor 1",
    "Floor 2",
    "Floor 3",
    "Toilet 1",
    "Toilet 2",
    "Toilet 3",
    "Toilet 4",
    "Toilet 5",
    "Toilet 6",
    "Toilet 7",
    "Toilet 8",
    "Toilet 9",
    "Toilet 10",
    "Toilet 11",
    "Toilet 12",
    "Toilet 13",
    "Toilet 14",
    "Toilet 15",
    "Toilet 16",
    "Toilet 17",
    "Toilet 18",
    "Toilet 19",
    "Toilet 20",
]


class createCommonComplaint(BaseModel):
    title : str
    description : str
    category : constr(regex=r'^(electrical|carpentry|plumbing)$')
    location : constr(regex=r'^(bh1|bh2|bh3|gh)$')
    object : constr(regex=r'^(' + "|".join(commonCarpentryObjects + commonElectricalObjects + commonPlumbingObjects) + r')$')
    objectId : constr(regex=r'^(' + "|".join(possibleObjectId) + r')$')
    password : str

    @validator('title' , 'description')
    def trim_whitespace(cls, value:str):
        return value.strip()
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
    email: constr(regex=r'^(bcs|imt|img)_20[12][0-9][01][0-9][0-9]@iiitm\.ac\.in$')
# ------------------------------------------------------------------
