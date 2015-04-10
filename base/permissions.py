from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from invite.models import MembershipModel

from events.models import EventModel


def memberCheck(user_, event_):
	membership = MembershipModel.objects.filter(user=user_, event=event_)
	for entry in membership:
		if entry.status == "Member" or "Coplanner" or "Creator":
			return True
		else:
			return False
	return False
	
def getMemberStatus(user_, event_):
	membership = MembershipModel.objects.filter(user=user_, event=event_)
	return membership.status


def isMember(user_, event_):
	membership = MembershipModel.objects.filter(user=user_, event=event_)
	if membership.status == "Member":
		return True
	else:
		return False

def isCoplanner(user_, event_):
	membership = MembershipModel.objects.filter(user=user_, event=event_)
	if membership.status == "Coplanner":
		return True
	else:
		return False

def isCreator(user_, event_):
	membership = MembershipModel.objects.filter(user=user_, event=event_)
	if membership.status == "Creator":
		return True
	else:
		return False


