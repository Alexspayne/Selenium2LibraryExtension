*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Page Contains Elements
    Wait Until Page Contains Elements    2s    id=input_01    id=input_02

Page Does Not Contain Elements
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Wait Until Page Contains Elements    2s    id=input_08    id=input_09
    Should Contain    ${ErrorMsg}    Element 'id=input_08' couldn't be found
