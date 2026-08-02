import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class NotificationsScreen extends StatelessWidget {
  const NotificationsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Notifications & Reminders')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: Icon(Icons.notifications_active_rounded, color: AppColors.accentOrange),
              title: Text('Spaced Revision Reminder', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('BST Traversal concept retention is at 78%. Tap to start 5-min review.', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
