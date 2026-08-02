import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class AdminUserManagementScreen extends StatelessWidget {
  const AdminUserManagementScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('User Management & RBAC Matrix')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: CircleAvatar(backgroundColor: AppColors.accentTeal, child: Icon(Icons.person_rounded, color: Colors.white)),
              title: Text('Alex Rivera (Student)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Role: student • Active • Email: alex@backtrace.ai', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
          SizedBox(height: 12),
          AppCard(
            child: ListTile(
              leading: CircleAvatar(backgroundColor: AppColors.accentCyan, child: Icon(Icons.co_present_rounded, color: Colors.white)),
              title: Text('Dr. Smith (Teacher)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Role: teacher • Active • Email: smith@backtrace.ai', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
