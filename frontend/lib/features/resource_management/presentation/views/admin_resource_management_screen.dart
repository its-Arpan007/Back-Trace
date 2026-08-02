import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdminResourceManagementScreen extends StatelessWidget {
  const AdminResourceManagementScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Educational Resource Library CMS')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.video_library_rounded, color: AppColors.accentTeal),
              title: Text('Interactive Array Offset Visualizer', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Type: Interactive WebApp • Target Concept: DSA_ARRAYS_01 • Language: English', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
