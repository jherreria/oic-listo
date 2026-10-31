import 'package:flutter/material.dart';

void main() {
  runApp(const OicListoApp());
}

class OicListoApp extends StatelessWidget {
  const OicListoApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'OIC Listo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepOrange),
        useMaterial3: true,
      ),
      home: const Scaffold(
        body: Center(
          child: Text(
            '<. OIC Listo\n(Flutter scaffold ready)',
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 24),
          ),
        ),
      ),
    );
  }
}
