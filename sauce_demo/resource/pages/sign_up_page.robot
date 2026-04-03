*** Settings ***
Library     SeleniumLibrary
Resource    ../../locators/sign_up_locators.robot

*** Keywords ***
Sign Up To The Application
    [Documentation]     this registers the user
    [Arguments]     ${first_name}   ${last_name}    ${email}    ${password}

    Click Element    ${sign_up_link}
    Log    Clicking on signup link

    Input Text    ${first_name_field}    ${first_name}
    Log    Entering first name

    Input Text    ${last_name_field}    ${last_name}
    Log    Entering last name

    Input Text    ${email_field}    ${email}
    Log    Entering email

    Input Text    ${password_field}    ${password}
    Log    Entering password

    Click Element    ${create_btn}
    Log    Clicking on create

