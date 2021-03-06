*** Settings ***
Test Setup        Open Browser to Extension Page
Test Teardown     Close Browser
Resource          ../resource.robot

*** Test Cases ***
Focus is not Set
    Element Focus Should Not Be Set    id=input_01
    Element Focus Should Not Be Set    id=input_02
    Element Focus Should Not Be Set    id=input_03

Focus is Set
    Set Element Focus    id=input_01
    ${ErrorMsg}=    Run Keyword And Expect Error    *    Element Focus Should Not Be Set    id=input_01
    Should Contain    ${ErrorMsg}    Element 'id=input_01' had focus while it shouldn't have
