import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdminAuditCenterScreen extends StatelessWidget {
  const AdminAuditCenterScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('System Audit Log Center')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.history_rounded, color: AppColors.accentTeal),
              title: Text('Action: UPDATE_AI_CONFIG (prompt_templates)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('User: Admin (33333333-3333-3333-3333-333333333333) • IP: 127.0.0.1', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
