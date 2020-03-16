# Created by lena at 3/14/2020
Feature: Test for H&M Search functionality

  Scenario: User can choose a product color
  Given Open H&M page
  When Search product Skirts
  Then Click item of the 4
  Then Menu will have 6 items
  When Click black
  When Select size
  When Add Skirts to the cart