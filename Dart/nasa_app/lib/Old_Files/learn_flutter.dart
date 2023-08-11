import 'package:flutter/material.dart';

class LearnFlutterPage extends StatefulWidget {
  const LearnFlutterPage({super.key});

  @override
  State<LearnFlutterPage> createState() => LearnFlutterPageState();
}

class LearnFlutterPageState extends State<LearnFlutterPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Mission Control"),
        automaticallyImplyLeading: false,
        leading: IconButton(
          onPressed: () {
            Navigator.of(context).pop();
          },
          icon: const Icon(Icons.home),
        ),
      ),
      body: Column(
        children: [
          Image.asset(
            'images/planets.jpg',
            height: 300,
          ),

          const SizedBox(
            height: 10,
          ),
          const Divider(
            color: Colors.black,
          ),
          Container(
            color: Colors.green,
            margin: const EdgeInsets.all(10.0),
            padding: const EdgeInsets.all(10.0),
            width: double.infinity,
            child: const Center(
              child: Text(
                'This is a text widget',
                style: TextStyle(color: Colors.white),
              ),
            ),
          ),
          ElevatedButton(
            onPressed: () {},
            child: const Text('Bravo Six, Going Dark'),
          ),
          // OutlinedButton(
          //   onPressed: () {},
          //   child: const Text('Button 2'),
          // ),
          // TextButton(
          //   onPressed: () {},
          //   child: const Text('Button 3'),
          // ),
        ],
      ),
    );
  }
}
