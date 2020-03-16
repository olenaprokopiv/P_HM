# Created by lena at 3/6/2020
Feature: Test for H&M Search functionality

  Scenario: Shopping cart - empty state
  Given Open H&M page
  When Click cart button
  Then Verify cart title YOUR SHOPPING BAG IS EMPTY!