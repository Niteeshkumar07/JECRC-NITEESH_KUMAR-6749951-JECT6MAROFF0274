*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  https://www.amazon.in/

*** Test Cases ***
Amazon
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Location Should Contain    amazon.in
    Sleep    3s
    Click Element   xpath=//a[text()=" Electronics "]
    Sleep    3s
    Scroll Element Into View    xpath=//span[text()="HP H200 Wireless Headset"]
    Sleep    3s
    ${name}     Get Text    xpath=//span[text()="HP H200 Wireless Headset"]
    Sleep    3s

    Click Element    xpath=//span[text()="HP H200 Wireless Headset"]
    @{windows}  Get Window Handles
    Switch Window   ${windows}[0]

    ${price}    Get Text    xpath=//span[@class="a-price-whole"]
    Log To Console    Price=${price}
    ${dicount}  Get Text    xpath=//span[@class="apex-savings-container"]/span
    Log To Console    Discount=${dicount}
    Wait Until Element Is Visible    xpath=//span[@class="a-price a-text-price"]    10s
    ${actual}   Get Text    xpath=//span[@class="a-price a-text-price apex-basisprice-value"]/span[2]
    Log To Console    Actual price=${actual}

    Scroll Element Into View    id=add-to-cart-button
    Sleep    3s
    
    Click Element    id=add-to-cart-button
    Wait Until Element Is Visible    xpath=//a[@class="nav-a nav-a-2 nav-progressive-attribute"]
    Click Element    xpath=//a[@class="nav-a nav-a-2 nav-progressive-attribute"]
    Sleep    3s
    
    Close Browser

    