import 'package:flutter/material.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';

class TeacherStudentProfileScreen extends StatelessWidget {
  const TeacherStudentProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Individual Student Cognitive Profile')),
      body: ListView(
        padding: const EdgeInsets.all(24),
        children: const [
          AppCard(
            child: ListTile(
              leading: CircleAvatar(backgroundColor: AppColors.accentTeal, child: Icon(Icons.person_rounded, color: Colors.white)),
              title: Text('Jordan Lee (Student ID: s2)', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
              subtitle: Text('Mastery: 38% (Critical Risk) • Decay Rate: 35% • Target Misconception: MIS_OFFSET_01', style: TextStyle(color: AppColors.textSecondaryDark)),
            ),
          ),
        ],
      ),
    );
  }
}
