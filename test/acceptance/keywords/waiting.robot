*** Settings ***
Documentation     Tests waiting
Test Setup        Go To Page "javascript/delayed_events.html"
Resource          ../resource.robot
Force Tags        Known Issue Internet Explorer

*** Test Cases ***
Wait For Condition
    [Documentation]    Wait For Condition
    Title Should Be    Original
    Wait For Condition    return window.document.title == "Changed"
    Run Keyword And Expect Error
    ...    Condition 'return window.document.title == "Invalid"' did not become true in 100 milliseconds
    ...    Wait For Condition    return window.document.title == "Invalid"    ${0.1}

Wait Until Page Contains
    [Documentation]    Wait Until Page Contains
    Wait Until Page Contains    New Content    2 s
    Run Keyword And Expect Error    Text 'invalid' did not appear in 100 milliseconds
    ...    Wait Until Page Contains    invalid    0.1

Wait Until Page Does Not Contain
    [Documentation]    Wait Until Page Does Not Contain
    Wait Until Page Does Not Contain    This is content    2 s
    Run Keyword And Expect Error    Text 'Initially hidden' did not disappear in 100 milliseconds
    ...    Wait Until Page Does Not Contain    Initially hidden    0.1

Wait Until Page Contains Element
    [Documentation]    Tests also that format characters (e.g. %c) are handled correctly in error messages
    Wait Until Page Contains Element    new div    2 seconds
    Run Keyword And Expect Error    Element '%cnon-existent' did not appear in 100 milliseconds
    ...    Wait Until Page Contains Element    %cnon-existent    0.1 seconds

Wait Until Page Does Not Contain Element
    [Documentation]    Tests also that format characters (e.g. %c) are handled correctly in error
    ...    messages
    Wait Until Page Does Not Contain Element    not_present    2 seconds
    Run Keyword And Expect Error    Element 'content' did not disappear in 100 milliseconds
    ...    Wait Until Page Does Not Contain Element    content    0.1 seconds

Wait Until Element Is Visible
    [Documentation]    Wait Until Element Is Visible
    Run Keyword And Expect Error    Element 'hidden' was not visible in 100 milliseconds
    ...    Wait Until Element Is Visible    hidden    0.1
    Wait Until Element Is Visible    hidden    2 s
    Run Keyword And Expect Error
    ...    Element locator 'invalid' did not match any elements after 100 milliseconds
    ...    Wait Until Element Is Visible    invalid    0.1
    Run Keyword And Expect Error
    ...    User error message    Wait Until Element Is Visible    invalid    0.1
    ...    User error message

Wait Until Element Is Enabled
    [Documentation]    Wait Until Element Is Enabled
    Run Keyword And Expect Error    Element 'id=disabled' was not enabled in 100 milliseconds
    ...    Wait Until Element Is Enabled    id=disabled    0.1
    Wait Until Element Is Enabled    id=disabled    2 s
    Run Keyword And Expect Error
    ...    Element locator 'id=invalid' did not match any elements after 100 milliseconds
    ...    Wait Until Element Is Enabled    id=invalid    0.1
    Run Keyword And Expect Error    User error message    Wait Until Element Is Enabled
    ...    id=invalid    0.1    User error message

Wait Until Element Contains
    [Documentation]    Wait Until Element Contains
    Run Keyword And Expect Error
    ...    Text 'New' did not appear in 100 milliseconds to element 'id=content'. Its text was 'This is content'.
    ...    Wait Until Element Contains    id=content    New    0.1
    Wait Until Element Contains    content    New Content    2 s
    Wait Until Element Contains    content    New    2 s
    Run Keyword And Expect Error
    ...    User error message    Wait Until Element Contains
    ...    content    Error    0.1    User error message
    Run Keyword And Expect Error
    ...    ValueError: Element locator 'id=invalid' did not match any elements.
    ...    Wait Until Element Contains    id=invalid    content    0.1

Wait Until Element Does Not Contain
    [Documentation]    Wait Until Element Does Not Contain
    Run Keyword And Expect Error
    ...    Text 'This is' did not disappear in 100 milliseconds from element 'id=content'.
    ...    Wait Until Element Does Not Contain    id=content    This is    0.1
    Wait Until Element Does Not Contain    content    This is    2 s
    Wait Until Element Does Not Contain    id=content    content    2 s
    Run Keyword And Expect Error    User error message    Wait Until Element Does Not Contain
    ...    content    New Content    0.1    User error message

Wait Until Element Has Class
    [Tags]  S2Lext
    [Documentation]    Wait Until Element Has Class
    Run Keyword And Expect Error
    ...    Class 'new_class' did not appear in 100 milliseconds to element 'id=class_changer'. Its class(es) was '[u'old_class']'.
    ...    Wait Until Element Has Class    id=class_changer    new_class    0.1
    Wait Until Element Has Class    id=class_changer    new_class    2 s

Wait Until Element Does Not Have Class
    [Tags]  S2Lext
    [Documentation]    Wait Until Element Does Not Have Class
    Run Keyword And Expect Error
    ...    Class 'old_class' still appeared after 100 milliseconds in element 'id=class_changer'. Its class(es) were '[u'old_class']'.
    ...    Wait Until Element Does Not Have Class    id=class_changer    old_class    0.1
    Wait Until Element Does Not Have Class    id=class_changer    old_class    2 s

Wait Until Element Has Focus
    [Tags]  S2Lext
    [Documentation]    Wait Until Element Has Focus
    Run Keyword And Expect Error
    ...    Element 'id=next_focus' did not get focus after 100 milliseconds
    ...    Wait Until Element Has Focus    id=next_focus    0.1
    Wait Until Element Has Focus    id=next_focus    2 s

Wait Until Element Does Not Have Focus
    [Tags]  S2Lext
    [Documentation]    Wait Until Element Does Not Have Focus
    Run Keyword And Expect Error
    ...    Element 'id=auto_focus' still had focus after 100 milliseconds while it shouldn't have
    ...    Wait Until Element Does Not Have Focus    id=auto_focus    0.1
    Wait Until Element Does Not Have Focus    id=auto_focus    2 s
