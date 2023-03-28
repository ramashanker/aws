package com.rama.app.controller;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.servers.Server;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@OpenAPIDefinition(servers = {@Server(url = "/", description = "Calculator URL")})
@RestController
public class OperationController {

  @GetMapping("/addition")
  public long addition(@RequestParam("a") long a, @RequestParam("b") long b) {
    return a + b;
  }

  @GetMapping("/substraction")
  public long substraction(@RequestParam("a") long a, @RequestParam("b") long b) {
    return a - b;
  }

  @PostMapping("/multiplication")
  public long multiplication(@RequestParam("a") long a, @RequestParam("b") long b) {
    return a * b;
  }

  @PutMapping("/division")
  public long division(@RequestParam("a") long a, @RequestParam("b") long b) {
    return a / b;
  }

}
