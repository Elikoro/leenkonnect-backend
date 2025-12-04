from rest_framework_simplejwt.authentication import JWTAuthentication


class CookieJWTAuthentication(JWTAuthentication):
    """Read JWT from Authorization header OR fallback to httpOnly cookie.

    The parent JWTAuthentication returns early when no Authorization header
    is present, so we must implement authenticate() to check cookies.
    """

    def authenticate(self, request):
        # Try header first
        header = self.get_header(request)
        raw_token = None

        if header is not None:
            raw_token = self.get_raw_token(header)

        # If no header token, try cookie named 'access'
        if raw_token is None:
            raw_token = request.COOKIES.get('access')

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token
