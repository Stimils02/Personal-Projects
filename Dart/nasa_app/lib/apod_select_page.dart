import 'package:flutter/material.dart';
import 'package:nasa_app/apod.dart';
import 'package:provider/provider.dart';

class ApodProvider extends ChangeNotifier {
  double selectedValue = 0.0;
  void setApodPictureCount(double value) {
    if (value != selectedValue) {
      selectedValue = value;
      notifyListeners();
    }
  }
}

class SelectApodMenu extends StatelessWidget {
  const SelectApodMenu({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Apply Your APOD Filters: "),
      ),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            const Text("Select the numbers of pictures: "),
            const SliderMenu(
              min: 0.0,
              max: 20.0,
              divisions: 20,
              width: 300,
            ),
            Consumer<ApodProvider>(builder: (context, provider, child) {
              return ElevatedButton(
                  onPressed: () {
                    double selectedValue =
                        Provider.of<ApodProvider>(context, listen: false)
                            .selectedValue;
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => APOD(
                          numPictures: selectedValue,
                        ),
                      ),
                    );
                  },
                  child: const Text("Invoke APOD Api"));
            })
            // ElevatedButton(
            //     onPressed: () {}, child: const Text("Invoke APOD Api")),
          ],
        ),
      ),
    );
  }
}

class SliderMenu extends StatefulWidget {
  final double min;
  final double max;
  final int divisions;
  final double width;
  const SliderMenu({
    super.key,
    required this.min,
    required this.max,
    required this.divisions,
    required this.width,
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
          Provider.of<ApodProvider>(context, listen: false)
              .setApodPictureCount(value);
        },
        activeColor: Colors.blue, // set the active color of the slider
        inactiveColor: Colors.grey, // set the inactive color of the slider
      ),
    );
  }
}

// class ApodMenuItems extends StatefulWidget {
//   final List<String> options;
//   const ApodMenuItems({super.key, required this.options});

//   @override
//   State<ApodMenuItems> createState() => _ApodMenuItemsState();
// }

// class _ApodMenuItemsState extends State<ApodMenuItems> {
//   String? dropdownvalue;
//   @override
//   Widget build(BuildContext context) {
//     return DropdownButton<String>(
//       value: dropdownvalue,
//       onChanged: (String? newValue) {
//         setState(() {
//           dropdownvalue = newValue;
//         });
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
