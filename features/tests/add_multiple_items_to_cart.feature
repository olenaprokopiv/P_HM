# Created by lena at 3/7/2020
Feature: Test for H&M Search functionality

  Scenario: User is able to add multiple items to the Shopping Cart
  Given Open H&M page
  Then Close popup
  When Search product Blazers
  When Click image of the 1 item
  When Select size
  And Add Blazers to the cart
  Then Switch to product search page
  And Click item of the 2
  When Select size
  And Add Blazers to the cart
  Then Number of items in the cart is 2
  When Click cart button
  And Click remove item
  Then Number of items in the cart is 1
  When Select item 2
  Then Number of items in the cart is 2