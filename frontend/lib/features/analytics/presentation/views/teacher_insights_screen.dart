import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class TeacherInsightsScreen extends StatelessWidget {
  const TeacherInsightsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Teacher Class Intelligence Hub')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.group_rounded, color: AppColors.accentTeal, size: 36),
              title: Text('Class Performance Avg: 78%', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Intervention Candidates: 2 Students • Top Misconception: Array Stride Mismatch (MIS_OFFSET_01)', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
