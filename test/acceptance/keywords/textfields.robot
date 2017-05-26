*** Setting ***
Documentation     Test textfields
Test Setup        Go To Page "forms/prefilled_email_form.html"
Variables         variables.py
Resource          ../resource.robot
Force Tags        Known Issue Internet Explorer

*** Test Cases ***
Get Value From Text Field
    [Documentation]    Get Value From Text Field
    ${text} =    Get Value    name
    Should Be Equal    ${text}    Prefilled Name
    Clear Element Text    name
    ${text} =    Get Value    name
    Should Be Equal    ${text}    ${EMPTY}

Input Unicode In Text Field
    [Documentation]    Input Unicode In Text Field
    Input Text    name    ${unic_text}
    ${text} =    Get Value    name
    Should Be Equal    ${text}    ${unic_text}

Input Password
    [Documentation]    LOG 3 Typing password into text field 'password_field'
    [Setup]    Go To Page "forms/login.html"
    Input Text    username_field    username
    Input Password    password_field    password
    Submit Form
    Verify Location Is "forms/submit.html"

Press Key
  [Setup]  Go To Page "forms/login.html"
  Cannot Be Executed in IE
  Press Key    username_field    James Bon
  Press Key    username_field    \\100
  Textfield Value Should Be    username_field    James Bond
  Press Key    password_field    f
  Press Key    login_button    \\10
  Verify Location Is "forms/submit.html"

Attempt Clear Element Text On Non-Editable Field
    [Documentation]    Attempt Clear Element Text On Non-Editable Field
    Run Keyword And Expect Error    *    Clear Element Text    can_send_email

Send Keys
    [Documentation]    Send Keys
    [Tags]  S2Lext
    Focus  name=comment
    Wait Until Element Has Focus  name=comment
    Send Keys  Some New Text
    Blur  name=comment
    Wait Until Element Does Not Have Focus  name=comment
    Send Keys  Not Received Text
    Textarea Value Should Be  name=comment  Some New TextPrefilled text area

Blur
    [Documentation]    Blur
    [Tags]  S2Lext  test
    Focus  name=comment
    Wait Until Element Has Focus  name=comment
    Blur  name=comment
    Element Focus Should Not Be Set  name=comment
