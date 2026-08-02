import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class GoalDashboardScreen extends StatelessWidget {
  const GoalDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Goal Dashboard & Milestones')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.flag_circle_rounded, color: AppColors.accentTeal, size: 36),
              title: Text('Goal: Master Array Memory Stride Math', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Target Mastery: 85% • Current Progress: 65% • Est Days: 4', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
