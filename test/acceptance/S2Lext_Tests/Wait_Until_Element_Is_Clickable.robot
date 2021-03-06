*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Element Is Clickable
    Wait Until Element Is Clickable    id=button_01    8s
    Wait Until Page Contains Element    id=div_02

Element Is Not Clickable
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Wait Until Element Is Clickable    id=button_02    8s
    Should Contain    ${ErrorMsg}    Couldn't find the element 'id=button_02', click operation failed
