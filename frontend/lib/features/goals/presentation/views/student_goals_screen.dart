import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class StudentGoalsScreen extends StatelessWidget {
  const StudentGoalsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Learning Goals & Targets')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.flag_rounded, color: AppColors.accentTeal, size: 36),
              title: Text('Goal: Reach 85% Mastery in Array Memory Layout', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Target Date: August 10, 2026 • Completion: 75%', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
