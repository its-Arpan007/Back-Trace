import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class ClassManagementScreen extends StatelessWidget {
  const ClassManagementScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Class Roster & Mastery Heatmaps')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: CircleAvatar(backgroundColor: AppColors.accentTeal, child: Icon(Icons.class_rounded, color: Colors.white)),
              title: Text('Data Structures & Algorithms - Sec A', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('32 Students • Average Mastery: 78% • Learning Velocity: 1.42x', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
