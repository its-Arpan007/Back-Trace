import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class QuestionVersionHistoryScreen extends StatelessWidget {
  const QuestionVersionHistoryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Question Version Audit History')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          AppCard(
            child: ListTile(
              leading: const CircleAvatar(backgroundColor: AppColors.accentTeal, child: Text('1.0', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))),
              title: const Text('v1.0.0 (Published & Active)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: const Text('Updated root cause weights and misconception detection hints.', style: TextStyle(color: AppColors.textSecondaryDark)),
              trailing: const Icon(Icons.check_circle, color: AppColors.success),
            ),
          ),
        ],
      ),
    );
  }
}
