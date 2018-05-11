Feature: Adding new customers

  Scenario: the Add New button
    Given a web browser displays the "Customer List" panel
    When the user clicks the "Add New" button
    Then the "Add Customer" panel shows up

  Scenario: add a new customer
    Given a web browser displays the "Add Customer" panel
    When the user types all obligated values
      | first_name | last_name | email              | telephone | password | confirm |
      | David      | Gahan     | depeche@gmail.com  | 222333444 | heaven   | heaven  |
    And the user clicks the "Save" button
    Then the browser goes back to the Customer List panel
    And the added customer appears in the Customer List

  Scenario: unsuccessful adding, missing first name
    Given a web browser displays the "Add Customer" panel
    When the user does not enter the "first name"
      | last_name | email              | telephone | password | confirm |
      | Gahan     | depeche@gmail.com  | 222333444 | heaven   | heaven  |
    And the user clicks the "Save" button
    Then a warning message is displayed

  Scenario: unsuccessful adding, missing last name
    Given a web browser displays the "Add Customer" panel
    When the user does not enter the "last name"
      | first_name | email              | telephone | password | confirm |
      | David      | depeche@gmail.com  | 222333444 | heaven   | heaven  |
    And the user clicks the "Save" button
    Then a warning message is displayed

  Scenario: unsuccessful adding, missing email
    Given a web browser displays the "Add Customer" panel
    When the user does not enter the "email"
      | first_name | last_name | telephone | password | confirm |
      | David      | Gahan     | 222333444 | heaven   | heaven  |
    And the user clicks the "Save" button
    Then a warning message is displayed

  Scenario: unsuccessful adding, missing telephone
    Given a web browser displays the "Add Customer" panel
    When the user does not enter the "telephone"
      | first_name | last_name | email              | password | confirm |
      | David      | Gahan     | depeche@gmail.com  | heaven   | heaven  |
    And the user clicks the "Save" button
    Then a warning message is displayed

  Scenario: unsuccessful adding, missing password
    Given a web browser displays the "Add Customer" panel
    When the user does not enter the "password"
      | first_name | last_name | email              | telephone | confirm |
      | David      | Gahan     | depeche@gmail.com  | 222333444 | heaven  |
    And the user clicks the "Save" button
    Then a warning message is displayed

  Scenario: unsuccessful adding, missing password confirmation
    Given a web browser displays the "Add Customer" panel
    When the user does not enter the "confirm"
      | first_name | last_name | email              | telephone | password |
      | David      | Gahan     | depeche@gmail.com  | 222333444 | heaven   |
    And the user clicks the "Save" button
    Then a warning message is displayed

  Scenario: cancel the process
    Given a web browser displays the "Add Customer" panel
    When the user clicks the "Cancel" button
    Then the browser goes back to the Customer List panel

  Scenario: add a new customer with additional address
    Given a web browser displays the "Add Customer" panel
    And the user types all obligates values
      | first_name | last_name | email              | telephone | password | confirm |
      | Mathew     | Sahan     | regerte@gmail.com  | 555666777 | asdf     | asdf    |
    When the user clicks the "Add Address" button
    And the user types all obligated values for additional address
      | first_name | last_name | address1               | city  | country        | region |
      | Mathew     | Sahan     | Praha1, Imaginarni 545 | Praha | Czech Republic | Praha  |
    And the user clicks the "Save" button
    Then the browser goes back to the Customer List panel
    And the added customer appears in the Customer List
