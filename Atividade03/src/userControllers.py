from datetime import datetime, timedelta, timezone
from sqlmodel import Session, select
from fastapi import APIRouter, HTTPException, status, Depends

from src.models import BaseUser, User, SignUpUserRequest, SignInUserRequest
from src.database import get_engine

router = APIRouter()

