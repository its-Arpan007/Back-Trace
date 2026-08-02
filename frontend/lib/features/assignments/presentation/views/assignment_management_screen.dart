import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AssignmentManagementScreen extends StatelessWidget {
  const AssignmentManagementScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Assignment & Deadline Management')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.assignment_turned_in_rounded, color: AppColors.accentTeal),
              title: Text('Array Offset Remediation Assignment', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Class: Sec A • Due: Aug 10, 2026 • Submission Rate: 85%', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
