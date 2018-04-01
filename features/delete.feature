Feature: Deleting customers

  Scenario Outline: delete and existing customer
    Given a web browser displays the "Customer List" panel
    And it displays customer "<name>" with the mail "<email>"
    When the user selects the customer "<name>" with the mail "<email>"
    And the user clicks the Delete button
    Then the customer "<name>" with the mail "<email>" is no longer displayed
    Examples: Names of Customers
      |     name     |       email       |
      | David Gahan  | depeche@mode.com  |
      | Mathew Sahan | regerte@gmail.com |


  Scenario: delete all customers
    Given a web browser displays the "Customer List" panel
    When the user clicks the Select all button
    And the user clicks the Delete button
    Then the Customer List is empty
