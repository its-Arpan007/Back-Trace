import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AITeacherAssistantScreen extends StatelessWidget {
  const AITeacherAssistantScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Teacher AI Assistant')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.co_present_rounded, color: AppColors.accentCyan, size: 36),
              title: Text('Classroom Summary Assistant', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Summarizes class misconceptions and auto-generates remediation lesson plans.', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
