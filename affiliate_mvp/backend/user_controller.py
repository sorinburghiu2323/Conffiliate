# import re
#
# from affiliate_mvp.backend.validators import validate_keywords, validate_platform, validate_user_data, validate_password
# from affiliate_mvp.models import User, UserPlatform, Platform, Keyword, UserKeyword, UserType
#
#
# class TemporaryUserPlatform:
#     """
#     Class to be used for creation of a temporary user platform.
#     """
#     name = ""
#     link = ""
#
#     def __init__(self, name, link):
#         self.name = name
#         self.link = link
#
#
# def create_user_keywords(user, keywords):
#     """
#     Create user keywords.
#     :param user: User instance
#     :param keywords: string of keywords
#     :return: None
#     """
#     keywords = re.sub("[^\w]", " ", keywords).split() if keywords else []
#     for keyword in keywords:
#         if Keyword.objects.filter(name=keyword).exists():
#             keyword_obj = Keyword.objects.get(name=keyword)
#         else:
#             keyword_obj = Keyword.objects.create(name=keyword)
#         new_user_keyword = UserKeyword.objects.create(
#             user=user,
#             keyword=keyword_obj,
#         )
#
#
# def create_influencer_platforms(user, platforms):
#     """
#     Create platform relation for influencer.
#     :param user: User instance
#     :param platforms: TemporaryUserPlatform instance
#     :return:
#     """
#     for platform in platforms:
#         new_user_platform = UserPlatform.objects.create(
#             user=user,
#             platform=Platform.objects.get(name=platform.name),
#             link=platform.link,
#         )
#
#
# def create_user(name, email, phone, user_type, password,
#                 description=None, picture=None, avg_pay=None, keywords: str = None,
#                 known_as=None, audience_no=None, avg_views=None, platforms: [TemporaryUserPlatform] = None,
#                 business_name=None, business_link=None):
#     """
#     Create a user.
#     Validators are run beforehand: User is not created if they fail.
#     :param name: string - user's name
#     :param email: string - user's email
#     :param phone: string - user's phone number
#     :param user_type: string - user type: "influencer" or "business"
#     :param password: string - password
#     :param description: (optional) string - description
#     :param picture: (optional) file - user profile picture or business logo
#     :param avg_pay: (optional) string/int - pay in £
#     :param keywords: (optional) string - keywords separated by " " or ", "
#     :param known_as: (optional influencer) string - user's alias
#     :param audience_no: (optional influencer) string/int - user's audience number
#     :param avg_views: (optional influencer) string/int - user's average views
#     :param platforms: (optional influencer) List of TemporaryUserPlatform - user's platforms
#     :param business_name: (optional business) string - business name
#     :param business_link: (optional business) string - business link
#     :return: None
#     """
#     # Run validators.
#     if validate_user_data(name, email, phone) or validate_keywords(keywords) or validate_password(password):
#         print("Data could not be validated.")
#         return
#     if user_type == "influencer":
#         for platform in platforms:
#             if validate_platform(platform.name):
#                 print("Platform does not exist.")
#                 return
#     elif user_type == "business":
#         pass
#     else:
#         return
#
#     # Create user and userdata.
#     new_user = User.objects.create_user(
#         name=name,
#         email=email,
#         phone=phone,
#         user_type=UserType.INFLUENCER if user_type == "influencer" else UserType.BUSINESS,
#         description=description,
#         picture=picture,
#         audience_no=int(audience_no) if audience_no else None,
#         avg_views=int(avg_views) if avg_pay else None,
#         avg_pay=int(avg_pay) if avg_pay else None,
#         known_as=known_as,
#         business_name=business_name,
#         business_link=business_link,
#         password=password,
#     )
#     if user_type == "influencer":
#         create_influencer_platforms(new_user, platforms)
#     create_user_keywords(new_user, keywords)
