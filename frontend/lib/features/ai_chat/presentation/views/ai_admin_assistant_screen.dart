import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AIAdminAssistantScreen extends StatelessWidget {
  const AIAdminAssistantScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Admin AI Operations Assistant')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.admin_panel_settings_rounded, color: AppColors.accentOrange, size: 36),
              title: Text('Platform Analytics & Audit Summarizer', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Provides operational insights on platform health and curriculum coverage.', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
