import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:backtrace/theme/app_colors.dart';
import 'package:backtrace/widgets/app_card.dart';
import 'package:backtrace/widgets/status_badge.dart';
import 'package:backtrace/features/auth/presentation/controllers/auth_controller.dart';
import 'package:backtrace/features/profile/presentation/controllers/profile_controller.dart';

class ProfileScreen extends ConsumerStatefulWidget {
  const ProfileScreen({super.key});

  @override
  ConsumerState<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends ConsumerState<ProfileScreen> {
  @override
  void initState() {
    super.initState();
    Future.microtask(() => ref.read(profileProvider.notifier).fetchProfile());
  }

  @override
  Widget build(BuildContext context) {
    final profileState = ref.watch(profileProvider);
    final userRole = ref.watch(currentUserRoleProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('User Profile & IAM'),
        actions: [
          IconButton(
            icon: const Icon(Icons.settings_outlined),
            onPressed: () => context.push('/settings'),
          ),
          IconButton(
            icon: const Icon(Icons.logout_rounded, color: AppColors.error),
            onPressed: () async {
              await ref.read(authProvider.notifier).logout();
              if (mounted) context.go('/');
            },
          ),
        ],
      ),
      body: profileState.isLoading
          ? const Center(child: CircularProgressIndicator(color: AppColors.accentTeal))
          : SingleChildScrollView(
              padding: const EdgeInsets.all(24.0),
              child: Column(
                children: [
                  CircleAvatar(
                    radius: 44,
                    backgroundColor: AppColors.accentIndigo,
                    child: const Icon(Icons.person_rounded, size: 52, color: Colors.white),
                  ),
                  const SizedBox(height: 16),
                  Text(
                    profileState.profileData?['username'] ?? 'User Account',
                    style: Theme.of(context).textTheme.displayMedium?.copyWith(color: Colors.white),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    profileState.profileData?['email'] ?? 'email@backtrace.ai',
                    style: const TextStyle(color: AppColors.textSecondaryDark),
                  ),
                  const SizedBox(height: 12),
                  StatusBadge(
                    label: 'ROLE: ${(userRole ?? "student").toUpperCase()}',
                    isOnline: true,
                  ),
                  const SizedBox(height: 24),
                  AppCard(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('Account Overview', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16)),
                        const Divider(color: AppColors.darkBorder),
                        const SizedBox(height: 8),
                        _buildProfileRow('Account Status', profileState.profileData?['status'] ?? 'Active'),
                        _buildProfileRow('Email Verified', (profileState.profileData?['email_verified'] == true) ? 'Verified' : 'Pending'),
                        _buildProfileRow('Timezone', profileState.profileData?['timezone'] ?? 'UTC'),
                        _buildProfileRow('Language', profileState.profileData?['language'] ?? 'en'),
                      ],
                    ),
                  ),
                  const SizedBox(height: 16),
                  ElevatedButton.icon(
                    onPressed: () => context.push('/account-security'),
                    icon: const Icon(Icons.shield_outlined),
                    label: const Text('Account Security & Sessions'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppColors.darkCard,
                      minimumSize: const Size(double.infinity, 50),
                    ),
                  ),
                ],
              ),
            ),
    );
  }

  Widget _buildProfileRow(String title, String val) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6.0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(title, style: const TextStyle(color: AppColors.textSecondaryDark)),
          Text(val, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w600)),
        ],
      ),
    );
  }
}
