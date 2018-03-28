from django.conf.urls import patterns, url

from appsembler_api import views


urlpatterns = patterns(
    '',
    # user API
    url(r'^accounts/user_without_password', views.CreateUserAccountWithoutPasswordView.as_view(), name="create_user_account_without_password_api"),
    url(r'^accounts/create', views.CreateUserAccountView.as_view(), name="create_user_account_api"),
    url(r'^accounts/connect', views.UserAccountConnect.as_view(), name="user_account_connect_api"),
    url(r'^accounts/update_user', views.UpdateUserAccount.as_view(), name="user_account_update_user"),
    url(r'^accounts/get-user/(?P<username>[\w.+-]+)', views.GetUserAccountView.as_view(), name="get_user_account_api"),

    # Just like CourseListView API, but with search
    url(r'^search_courses', views.CourseListSearchView.as_view(), name="course_list_search"),

    # bulk enrollment API
    url(r'^bulk-enrollment/bulk-enroll', views.BulkEnrollView.as_view(), name="bulk_enrollment_api"),

    # enrollment codes API
    url(r'^enrollment-codes/generate', views.GenerateRegistrationCodesView.as_view(), name="generate_registration_codes_api"),
    url(r'^enrollment-codes/enroll-user', views.EnrollUserWithEnrollmentCodeView.as_view(), name="enroll_use_with_code_api"),
    url(r'^enrollment-codes/status', views.EnrollmentCodeStatusView.as_view(), name="enrollment_code_status_api"),

    # enrollment analytics API
    url(r'^analytics/accounts/batch', views.GetBatchUserDataView.as_view(), name="get_batch_user_data"),
    url(r'^analytics/enrollment/batch', views.GetBatchEnrollmentDataView.as_view(), name="get_batch_enrollment_data"),
)
