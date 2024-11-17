*** Settings ***
Resource  resource.robot
Resource    login.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testkalle
    Set Password  kalle123
    Set Repeat Password  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  kalle123
    Set Repeat Password  kalle123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  testman
    Set Password  kalle12
    Set Repeat Password  kalle12
    Submit Credentials
    Register Should Fail With Message  Password too short
# robot -t "Register With Valid Username And Too Short Password" src/tests/register.robot

Register With Valid Username And Invalid Password
# # salasana ei sisällä halutunlaisia merkkejä
    Set Username  testman
    Set Password  kallekalle
    Set Repeat Password  kallekalle
    Submit Credentials
    Register Should Fail With Message  Password can't be only letters

# robot -t "Register With Valid Username And Invalid Password" src/tests/register.robot

Register With Nonmatching Password And Password Confirmation
    Set Username  testman
    Set Password  kalle123
    Set Repeat Password  kalle12345
    Submit Credentials
    Register Should Fail With Message  Passwords dont match
# robot -t "Register With Nonmatching Password And Password Confirmation" src/tests/register.robot

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Repeat Password  kalle123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists
# robot -t "Register With Username That Is Already In Use" src/tests/register.robot

Login After Successful Registration
    Set Username  testkalle
    Set Password  kalle123
    Set Repeat Password  kalle123
    Submit Credentials
    Register Should Succeed
    Conitinue To Main Page
    Log Out
    Set Username  testkalle
    Set Password  kalle123
    Submit Login
    Login Should Succeed

# robot -t "Login After Successful Registration" src/tests/register.robot
# robot src/tests/login.robot

Login After Failed Registration
    Set Username  te
    Set Password  kalle123
    Set Repeat Password  kalle123
    Submit Credentials
    Register Should Fail With Message  Username too short
    Conitinue To Login Page
    Set Username  te
    Set Password  kalle123
    Submit Login
    Login Should Fail With Message  Invalid username or password
# robot -t "Login After Failed Registration" src/tests/register.robot

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Conitinue To Login Page
    Click Link  Login

Conitinue To Main Page
    Click Link  Continue to main page

Log Out
    Click Button  Logout

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
Submit Login
    Click Button  Login

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Repeat Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
