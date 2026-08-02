import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AppSettingsScreen extends StatelessWidget {
  const AppSettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Settings & Offline Sync')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.sync_rounded, color: AppColors.accentTeal),
              title: Text('Offline Cache & Background Sync', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Status: Offline Mode Ready • Queue: 0 Pending Attempts', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
