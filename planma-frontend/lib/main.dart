import 'package:flutter/material.dart';
import 'package:planma_app/authentication/log_in.dart';
void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: LogIn(),
      debugShowCheckedModeBanner: false,
    );
  }
}
