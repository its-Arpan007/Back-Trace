import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class RecommendedResourcesScreen extends StatelessWidget {
  const RecommendedResourcesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Recommended Learning Resources')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.ondemand_video_rounded, color: AppColors.accentTeal),
              title: Text('Interactive Visualizer: Array Memory Stride Math', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Type: Interactive Video • Match Score: 96% • Est Time: 10 mins', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
