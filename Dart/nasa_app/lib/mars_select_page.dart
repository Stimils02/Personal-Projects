import 'package:flutter/material.dart';
import 'package:nasa_app/data_storage.dart';
import 'package:nasa_app/mars_rover.dart';

class SelectMarsMenu extends StatelessWidget {
  const SelectMarsMenu({super.key});
  @override
  Widget build(BuildContext context) {
    // final List<String> cameraOptions = MarsOptions.cameraOptions;
    return Scaffold(
      appBar: AppBar(
        title: const Text("Apply Your Mars Filters: "),
      ),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            // const Text("Select A Camera: "),
            // DropDownMenu(
            //   options: cameraOptions,
            // ),
            const Text("Select which Sol you want the pictures from: "),
            const SliderMenu(
              min: 0.0,
              max: 1000.0,
              divisions: 100,
              width: 300.0,
              type: "Sol",
            ),
            const Text("Select the number of pictures: "),
            const SliderMenu(
              min: 0.0,
              max: 10,
              divisions: 10,
              width: 200.0,
              type: "Pics",
            ),
            ElevatedButton(
                onPressed: () {
                  Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => MarsRover(
                                // cameraSelected: MarsOptions.cameraSelected,
                                sol: MarsOptions.sol,
                                numPicture: MarsOptions.numPictures,
                              )));
                },
                child: const Text("Invoke Mars Api")),
          ],
        ),
      ),
    );
  }
}

// class DropDownMenu extends StatefulWidget {
//   final List<String> options;
//   const DropDownMenu({super.key, required this.options});

//   @override
//   State<DropDownMenu> createState() => DropDownMenuState();
// }

// class DropDownMenuState extends State<DropDownMenu> {
//   String? dropdownvalue;
//   @override
//   Widget build(BuildContext context) {
//     return DropdownButton<String>(
//       value: dropdownvalue,
//       onChanged: (String? newValue) {
//         setState(() {
//           dropdownvalue = newValue;
//         });
//         MarsOptions.cameraSelected = newValue;
//       },
//       items: widget.options.map<DropdownMenuItem<String>>((String option) {
//         return DropdownMenuItem<String>(
//           value: option,
//           child: Text(option),
//         );
//       }).toList(),
//     );
//   }
// }

class SliderMenu extends StatefulWidget {
  final double min;
  final double max;
  final int divisions;
  final double width;
  final String type;
  const SliderMenu({
    super.key,
    required this.min,
    required this.max,
    required this.divisions,
    required this.width,
    required this.type,
  });

  @override
  State<SliderMenu> createState() => _SliderMenuState();
}

class _SliderMenuState extends State<SliderMenu> {
  double sliderValue = 0.0;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: widget.width,
      height: 30.0,
      child: Slider(
        value: sliderValue,
        min: widget.min,
        max: widget.max,
        divisions: widget.divisions,
        label: sliderValue.round().toString(),
        onChanged: (double value) {
          setState(() {
            sliderValue = value;
          });
          if (widget.type == "Sol") {
            MarsOptions.sol = value;
          } else if (widget.type == "Pics") {
            MarsOptions.numPictures = value;
          }
        },
        activeColor: Colors.blue, // set the active color of the slider
        inactiveColor: Colors.grey, // set the inactive color of the slider
      ),
    );
  }
}
