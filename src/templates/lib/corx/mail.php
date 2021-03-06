<?php
	require_once(realpath(__DIR__ . '/../..').'/config.php');

	// Get owner
	$jobData = json_decode($argv[1], true);
	$owner = $jobData['owner'];
	$hash_id = $jobData['hash_id'];

	// Send mail
	// Send verification email
	$mail = new PHPMailer(true);

	try {

		if(!$argv) {
			throw new Exception('No arguments supplied.');
		}

		// Construct mail
		$mail_generator = new \LotusBase\MailGenerator();
		$mail_generator->set_title('<em>Lotus</em> Base: CORNEA Job Completed');
		$mail_generator->set_header_image('cid:mail_header_image');
		$mail_generator->set_content(array(
			'<h3 style="text-align: center; ">Your CORNEA job has been completed</h3>
			<p>Your CORNEA job with the following ID: <strong>'.$hash_id.'</strong> has been successfully completed. Your job file will be stored on our servers for a total of 30 days, after which it will be removed. We strongly encourage users to download the gzipped JSON file which contains all the data from your CORNEA job.</p>
			<p>You may view your job at the following URL: <a href="'.DOMAIN_NAME.WEB_ROOT.'/tools/cornea/job/'.$hash_id.'">'.DOMAIN_NAME.WEB_ROOT.'/tools/cornea/job/'.$hash_id.'</a></p>
			<p>Your job file (<strong>'.human_filesize(filesize(DOC_ROOT.'/data/cornea/jobs/'.$hash_id.'.json.gz')).'</strong>) can be downloaded from <a href="'.DOMAIN_NAME.WEB_ROOT.'/api/v1/cornea/job/data/'.$hash_id.'">'.DOMAIN_NAME.WEB_ROOT.'/api/v1/cornea/job/data/'.$hash_id.'</a>. This file will expire in 30 days.</p>
			'));

		$mail->IsSMTP();
		$mail->IsHTML(true);
		$mail->Host			= SMTP_MAILSERVER;
		$mail->AddReplyTo($owner, $owner);
		$mail->SetFrom(NOREPLY_EMAIL, 'Lotus Base');
		$mail->CharSet		= "utf-8";
		$mail->Encoding		= "base64";
		$mail->Subject		= "Lotus Base: CORNEA Job Completed ";
		$mail->AltBody		= "To view the message, please use an HTML compatible email viewer.";
		$mail->MsgHTML($mail_generator->get_mail());
		$mail->AddAddress($owner, $owner);

		$mail->AddEmbeddedImage(DOC_ROOT."/dist/images/mail/header_cornea.jpg", mail_header_image);
		$mail->smtpConnect(
			array(
				"ssl" => array(
					"verify_peer" => false,
					"verify_peer_name" => false,
					"allow_self_signed" => true
				)
			)
		);

		$mail->Send();

		// Mail successfully sent
		echo json_encode(array('success' => true, 'message' => 'Mail successfully sent.'));

	} catch(phpmailerException $e) {
		// Mail has failed to send
		echo json_encode(array('error' => true, 'message' => $e->errorMessage()));
	} catch(Exception $e) {
		// General exception
		echo json_encode(array('error' => true, 'message' => $e->errorMessage()));
	}
?>