from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user: object) -> hash:
    """Create manually token for user

    Args:
        user (object)

    Returns:
        hash
    """
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
