# Created by lena at 3/6/2020
Feature: Test for H&M Search functionality

  Scenario: Verify that Sign in with existing account works
  Given Open H&M page
  When Click on Sign in
  When Input signin email Pppprrrr2@gmail.com
  And Input signin password Pppprrrr2
  And Click on the SIGN IN
  And Click on the My Account
  Then Results for Pppprrrr2@gmail.com is shown