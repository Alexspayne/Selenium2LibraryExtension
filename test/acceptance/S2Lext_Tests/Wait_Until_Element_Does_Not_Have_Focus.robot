*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Does Not Have Focus
    Wait Until Element Does Not Have Focus    id=input_01

Has Focus
    Set Element Focus    id=input_01
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Wait Until Element Does Not Have Focus    id=input_01    3s
    Should Contain    ${ErrorMsg}    Element 'id=input_01' still had focus after 3 seconds while it shouldn't have
