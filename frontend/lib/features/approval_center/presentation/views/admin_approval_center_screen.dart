import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdminApprovalCenterScreen extends StatelessWidget {
  const AdminApprovalCenterScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Content Approval Queue')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.fact_check_rounded, color: AppColors.accentCyan),
              title: Text('Pending Approval: Array Offset Multiplication Question', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Requested by: Dr. Smith • Item Type: Question', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
