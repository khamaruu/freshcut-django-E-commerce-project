def admin_only(user):
    return user.is_authenticated and user.is_staff
