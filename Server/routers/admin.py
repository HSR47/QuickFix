
from fastapi import APIRouter , status , HTTPException , Depends
from Server.database import getdb
from Server.routers.auth import getCurrentUser
from sqlalchemy.orm.session import Session

import Server.config as config
import Server.utils as utils
import Server.schemas as schemas
import Server.models as models

adminRouter = APIRouter(tags=["Admin"])

# ----------------------------CREATE ADMIN-------------------------
@adminRouter.post("/admin" , response_model=schemas.returnAdmin)
def signupAdmin(data : schemas.signupAdmin , db:Session = Depends(getdb)):

    check = db.query(models.Admin)
    check = check.filter(models.Admin.email == data.email)
    check = check.first()
    if check != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="Admin with this email alreay exits")

    newAdmin = models.Admin(
        name = data.name,
        email = data.email,
        hostel = data.hostel,
        password = utils.hashPassword(data.password)
    )

    db.add(newAdmin)
    db.commit()
    db.refresh(newAdmin)

    return newAdmin
# ------------------------------------------------------------------


# ----------------------------GET ALL ADMINS-------------------------
@adminRouter.get("/admin" , response_model=list[schemas.returnAdmin])
def getAllAdmins(db:Session = Depends(getdb) , user = Depends(getCurrentUser)):

    allAdmins = db.query(models.Admin).all()
    return allAdmins
# ------------------------------------------------------------------


# ----------------------------GET MY DETAILS (ADMIN)-------------------------
@adminRouter.get("/admin/me" , response_model=schemas.returnAdmin)
def getMyDetailsAdmin(admin:models.Admin = Depends(getCurrentUser) , db:Session = Depends(getdb)):

    if not isinstance(admin , models.Admin):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="You are not an admin")

    return admin
# ------------------------------------------------------------------


# ----------------------------GET SPECIFIC ADMIN-------------------------
@adminRouter.get("/admin/{id}" , response_model=schemas.returnAdmin)
def getSpecificAdmin(id:int , db:Session = Depends(getdb)):

    admin = db.query(models.Admin)
    admin = admin.filter(models.Admin.id == id)
    admin = admin.first()

    if admin == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Admin with this id doesn't exist")

    return admin
# ------------------------------------------------------------------


# ----------------------------UPDATE ADMIN PROFILE-------------------------
@adminRouter.put("/admin/me" , response_model=schemas.returnAdmin)
def updateadminProfile(data:schemas.updateAdmin , admin:models.Admin = Depends(getCurrentUser) , db:Session = Depends(getdb)):
    if not isinstance(admin , models.Admin):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="Not allowed")
    
    if data.name != None:
        admin.name = data.name
    if data.hostel != None:
        admin.hostel = data.hostel

    db.commit()
    db.refresh(admin)

    return admin
# ------------------------------------------------------------------
