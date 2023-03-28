package com.rama.app.controller;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class OperationControllerTest {

  @Test
  public void addTest() {
    OperationController operationController = new OperationController();
    long result = operationController.addition(5, 6);
    Assertions.assertEquals(result, 11);
  }

  @Test
  public void subTest() {
    OperationController operationController = new OperationController();
    long result = operationController.substraction(11, 6);
    Assertions.assertEquals(result, 5);
  }

  @Test
  public void mulTest() {
    OperationController operationController = new OperationController();
    long result = operationController.multiplication(3, 6);
    Assertions.assertEquals(result, 18);
  }

  @Test
  public void divisionTest() {
    OperationController operationController = new OperationController();
    long result = operationController.division(12, 6);
    Assertions.assertEquals(result, 2);
  }

}
