# Created by lena at 3/6/2020
Feature: Test for H&M Search functionality

  Scenario: User is able to add an item to the Shopping Cart
  Given Open H&M page
  When Search product Blazers
  When Click image of the first item
  When Select size
  And Add Blazers to the cart
  Then Number of items in the cart more than zero